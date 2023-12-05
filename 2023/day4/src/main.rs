use std::{fs, collections::HashMap};

fn part1() {
    let content  = fs::read_to_string("src/input.txt").unwrap();
    let lines : Vec<&str> = content.split("\n").collect();
    
    let mut sum : u32 =0;
    for line in lines {
        let game_split : Vec<&str> = line.split(":").collect(); 
        let arr_src : Vec<&str>  = game_split[1].split("|").collect();
        let arr1_src : Vec<&str> = arr_src[0].trim().split(" ").collect();
        let arr2_src : Vec<&str> = arr_src[1].trim().split(" ").collect();
        
        let mut arr1 : Vec<u32> = vec![];
        let mut arr2 : Vec<u32> = vec![];
        
        for num in arr1_src { 
            if !num.trim().to_string().eq("") && num.trim().to_string().chars().nth(0).unwrap().is_numeric() {
                arr1.push(num.trim().parse::<u32>().unwrap());
            }
        }
        for num in arr2_src {
            if !num.trim().to_string().eq("") && num.trim().to_string().chars().nth(0).unwrap().is_numeric() {
                arr2.push(num.trim().parse::<u32>().unwrap());
            }
        }

        let mut mult = 0;
        for num in arr1 {
            match arr2.iter().position(|&r| r == num) {
                Some(i) => {
                    if mult == 0 {
                        mult = 1;
                    } else {
                        mult *= 2;
                    }
                    arr2.remove(i);
                }, 
                None => (),
            } 
        }

        sum += mult;
    }

    println!("total worth of points: {}",sum);
}

fn main() {
    part1()
}
