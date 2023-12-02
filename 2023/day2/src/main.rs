use std::{fs, collections::HashMap};

fn part1() {
    let content = fs::read_to_string("./src/input.txt").expect("failed to load filed");
    let lines : Vec<&str> = content.split("\n").collect();

    let mut sum = 0;

    for line in lines {
        let splited : Vec<&str> = line.split(":").collect(); 

        let a : Vec<&str>  = splited[0].split(" ").collect();
        let id = a[1].parse::<u32>().unwrap();
        let sets : Vec<&str>  = splited[1].split(";").collect();



        let mut is_valid = true;
        for set in sets {
            let cubes : Vec<&str> =  set.split(",").collect();
            let mut acc: HashMap<String, u32>  = HashMap::new();

            println!("{} {:?}",set,cubes);

            for cube in cubes {
                let splited : Vec<&str> =  cube.trim().split(" ").collect();

                let count = splited[0].parse::<u32>().unwrap();
                let key  = splited[1].to_string();

                match acc.get(&key) {
                    Some(val) => {
                        acc.insert(key, val + count);
                    }
                    None => {
                        acc.insert(key, count);
                    }
                }
            }
            println!("{:?}",acc);

            let red = match acc.get("red") {
                Some(val) => *val,
                None => 0,
            };
            let blue = match acc.get("blue") {
                Some(val) => *val,
                None => 0,
            };
            let green = match acc.get("green") {
                Some(val) => *val,
                None => 0,
            };
            
            if red > 12 || green > 13 ||  blue > 14 {
                is_valid = false;
                break;
            }
        }
        if is_valid {
            sum += id;
        }
        
    }
    println!("{}",sum);

}

fn main() {
    part1()
}
