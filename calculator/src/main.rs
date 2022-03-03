use std::io::{stdin, stdout, Write};

fn read(input: &mut String) {
    stdout().flush().expect("failed to flush");
    stdin().read_line(input).expect("failed to flush");
}

fn main() {
    println!("WARNING! THIS CODE IS VERY BAD! YOU HAVE BEEN WARNED");
    let mut num1 = String::new();
    let mut num2 = String::new();
    let mut operator = String::new();
    let mut str_exit = String::new();

    loop {
        println!("my name is muchamad, this is me calculator, say continue to continue to calculate and exit to exit");

        std::io::stdin()
            .read_line(&mut str_exit)
            .expect("could not read input");

        println!("what is the first number?:");
        read(&mut num1);

        println!("what is the second number?:");
        read(&mut num2);

        println!("what is the operator?:");
        read(&mut operator);

        println!("{} {} {}", num1, operator, num2);

        let num1: f32 = num1.trim().parse().unwrap();
        let num2: f32 = num2.trim().parse().unwrap();
        let operator: char = operator.trim().chars().next().unwrap();
        let operator_contain = String::from("+-*/");

        if !operator_contain.contains(operator) {
            println!("fuck you dont cheat the system you cant run away with it so just play along with everyone else");
            break;
        }

        let resault = match operator {
            '+' => num1 + num2,
            '*' => num1 * num2,
            '/' => num1 / num2,
            '-' => num1 - num2,
            _ => panic!("error in operator"),
        };
        println!("resaults: {} {} {} = {}", num1, operator, num2, resault);
    }
}
