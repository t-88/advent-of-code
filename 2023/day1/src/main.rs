use std::fs;

fn part1() {
    let contents = fs::read_to_string("./src/input.txt").expect("smth wrong with input file");
    let lines = contents.split("\n").collect::<Vec<&str>>();
    
    let mut sum = 0;
    println!("numbers:");
    for line in lines {
        let mut first: u32  = 69;
        let mut last : u32  = 0;
        for chr in line.chars() {
            if chr.is_numeric() {
                if first == 69 {
                    first = chr as u32 - '0' as u32;
                }
                last = chr as u32 - '0' as u32;
            }
        }
        println!("  {}",first * 10 + last);
        sum += first * 10 + last;
    }
    println!("sum: {}",sum);
}

fn part2() {
    let contents = fs::read_to_string("./src/input.txt").expect("smth wrong with input file");
    let lines = contents.split("\n").collect::<Vec<&str>>();


    let number_map : Vec<&str> = vec![
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ];
    
    

    let mut sum = 0;
    println!("numbers:");
    for line in lines {
        let mut first: u32  = 69;
        let mut last : u32  = 0;


        let mut acc  = line.to_string();

        for i in 0..number_map.len()  {
            let replaced_with = format!("{}{}{}",number_map[i].chars().nth(0).unwrap(),i + 1 ,number_map[i].chars().nth(number_map[i].len() - 1).unwrap());
            acc = acc.replace(number_map[i],  &replaced_with);
        }

        
        for chr in acc.chars() {
            if chr.is_numeric() {
                if first == 69 {
                    first = chr as u32 - '0' as u32;
                }
                last = chr as u32 - '0' as u32;
            } 
        }

        

        assert_ne!(first,69,"first should not equal 69 at the end"); // this means nothing overrides first
        println!("{}  {}",line,first * 10 + last);
        sum += first * 10 + last;
    }

        println!("sum: {}",sum);
}


fn main() {
    part1()
}
