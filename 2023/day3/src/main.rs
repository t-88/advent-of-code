use std::{fs, collections::HashMap};


fn get_number(nums : &mut HashMap<u32,String>, idx : u32) -> u32 {
    let out =  match nums.get(&idx) {
        Some(val) =>  val.parse::<u32>().unwrap(),
        None => 0
    };
    
    if out != 0 {
        if let Some(val) = nums.get(&(idx + (nums.get(&idx).unwrap().len() - 1) as u32))   {
            if (*val).eq(nums.get(&idx).unwrap()) {
                *nums.get_mut(&(idx + (val.len() - 1) as u32 )).unwrap() = "0".to_string();
            }
        } else {
        }
        if  let Some(val) = nums.get(&(idx - (nums.get(&idx).unwrap().len() - 1) as u32 ))   {
            if (*val).eq(nums.get(&idx).unwrap()) {
                *nums.get_mut(&(idx - (val.len() - 1) as u32 )).unwrap() = "0".to_string();
            }
        }            

        *nums.get_mut(&idx).unwrap() = "0".to_string(); 
    }
    out
}

fn part1() {
    let content = fs::read_to_string("src/input.txt").unwrap();

    let lines : Vec<&str> = content.split("\n").collect();
    
    let width = lines[0].len();
    let height = lines.len();


    let mut nums : HashMap<u32,String> = HashMap::new();

    for j in 0..lines.len() {
        let mut i = 0;
        let line = lines[j]; 
        while i < line.len() {
            let chr = line.chars().nth(i).unwrap();
            i += 1;
            if chr.is_numeric() {
                let start = i - 1;
                
                let mut number : String = String::new();
                number.push(chr);
                while i < width && line.chars().nth(i).unwrap().is_numeric() {
                    number.push(line.chars().nth(i).unwrap());
                    i += 1;
                }
                nums.insert((j * width + start) as u32,   number.clone());
                nums.insert((j * width + start + number.len() - 1) as u32, number.clone());
            }
        }
    }


    let mut sum : u32 = 0;

    for j in 0..lines.len() {
        for (idx,chr) in lines[j].chars().enumerate() {
            if chr != '.' && !chr.is_numeric() {
                if idx > 0 {
                    sum += get_number(&mut nums,(idx + j * width - 1) as u32);
                }
                if idx < width {
                    sum += get_number(&mut nums,(idx + j * width + 1) as u32);
                }
                if j > 0 {
                    sum += get_number(&mut nums,(idx + (j - 1) * width) as u32);
                    if idx > 0 { 
                        sum += get_number(&mut nums,(idx + (j - 1) * width - 1) as u32); 
                    }
                    if idx < width { 
                        sum += get_number(&mut nums,(idx + (j - 1) * width + 1) as u32); 
                    }
                    
                }
                if j < height {
                    sum += get_number(&mut nums,(idx + (j + 1) * width) as u32);
                    if idx > 0 {
                        sum += get_number(&mut nums,(idx + (j + 1) * width - 1) as u32); 
                    }
                    if idx < width {
                        sum += get_number(&mut nums,(idx + (j + 1) * width + 1) as u32); 
                    }

                }

            }
        }
    }


    
    println!("sum: {}",sum);

}
    

fn main() {
    part1()

}
