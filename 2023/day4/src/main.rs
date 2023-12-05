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


fn part2() {
    println!("dont worry its takes time ;)");

    let content  = fs::read_to_string("src/input.txt").unwrap();
    let lines : Vec<&str> = content.split("\n").collect();
    
    let mut sum : u32 =0;

    let mut cards : HashMap<u32,u32> = HashMap::new();

    let mut parsed_cards : Vec<(Vec<u32>,Vec<u32>,u32,i32)> = vec![];
    for line in lines {
        let game_split : Vec<&str> = line.split(":").collect(); 
        let card : Vec<&str> = game_split[0].split("Card").collect();
        let card_id = card[1].trim().parse::<u32>().unwrap();

        cards.insert(card_id,1);

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

        
        parsed_cards.push( (arr1,arr2,1,-1));
    }

    for card in 0..parsed_cards.len() {
        for _ in 0..parsed_cards[card].2 { // rust :O
            // should cache the resualt  
            let mut cards_count = 0; 
            for num in &parsed_cards[card].0 {
                cards_count += match parsed_cards[card].1.iter().position(|&r| r == *num) {
                    Some(_) =>  1,
                    None => 0,
                } 
            }
            
            for i in 0..cards_count {
                parsed_cards[card + i + 1].2 += 1;
            }
        }
    }
    for card in parsed_cards {
        sum += card.2;
    }

    println!("sum: {:?}",sum);
}

fn main() {
    part2()
}
