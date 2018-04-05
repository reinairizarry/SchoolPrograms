//Reina Irizarry
//This program creates multiplication and addition flash cards for little kids.

import java.util.Scanner;
import java.util.Random;

public class mathTutor {
	public static void main(String[] args) {
		
		//Import libraries  and declare our variables
		Random rnd = new Random();
		Scanner sc = new Scanner(System.in);
		int Choice, Problem, Num, Result, Op,Num1,Num2, Correct, Answer;
		int Mixed, Numa,Numb,Numc, Numd;
		String doRandom;
		double Average;
		double toss = 0;
		boolean sumNumbers;
		
	   //Menu print statements: 
		 do {
			System.out.println("*********************");
			System.out.println("Electronic Math Tutor ");
			System.out.println("*********************");
			System.out.println("Choose the type of problem you want to practice: ");
			System.out.println("1. Addition");
			System.out.println("2. Multiplication ");
			System.out.println("3. Mixed ");
			System.out.println("4. Quit ");
			
			System.out.print("Enter your choice: ");
			Choice = sc.nextInt();
			System.out.print("How many problems? ");
			Problem = sc.nextInt();
			System.out.print("Largest operand? ");
			Op = sc.nextInt();
			Correct = 0;
			sumNumbers = true;
			
			//This will loop the menu
			for (int i = 1; i <= Problem; i++) { 
				//addition
				if (Choice == 1){
				sumNumbers = true;
		    		Num1 = rnd.nextInt(Op);//random numbers
		    		Num2 = rnd.nextInt(Op);
		    		Num = Num1 + Num2;
		    		System.out.println(Num1 + " + " + Num2 +" = ");
		    		Answer = sc.nextInt();
		    		
		    		//correct and incorrect if statements
		    		if (Answer != Num) {
		    			System.out.println("Incorrect, the answer is " + Num);			
		    		}
		    		else {
		    			System.out.println("Correct");
		    			Correct = Correct + 1;	    			
		    		}	
		    	//Multiplication 
		    }else if (Choice == 2){
		      	sumNumbers = false;
			    	Num1 = rnd.nextInt(Op);
		    		Num2 = rnd.nextInt(Op);
		    		Num = Num1 * Num2;
		    		System.out.println(Num1 + " * " + Num2 +" = ");
		    		Answer = sc.nextInt();
		    		
		    		//correct and incorrect if statements
		    		if (Answer != Num) {
		    			System.out.println("Incorrect, the answer is " + Num);		
		    		}
		    		else {
		    			System.out.println("Correct");
		    			Correct = Correct + 1;	    			
		    		}
		    		
		    }
			//Mixed 
		    else if (Choice == 3) {
		    	//addition	
		    	Numa = rnd.nextInt(Op);
	    		Numb = rnd.nextInt(Op);//program was working fine until i added this
	    		toss = rnd.nextDouble();
	    		//Numc = rnd.nextInt(Op);         
	    			if (toss <= 0.5) {
	    			sumNumbers = true;
	    			Choice = Numa + Numb;
	    			else if (toss >= 0.5) {
	    				
	    				
	    			}
	    		}
	    } 
           } // end of for loop
			
			//Correct counter and average 
			System.out.println("You answered " + Correct  + " out of " + Problem + " questions correctly");
			Average = (((double) Correct / Problem) * 100);
			System.out.println("Your average is "+ Average);
		    
		 } while (Choice !=4);
		
	}

}
