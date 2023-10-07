package com.company;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
/**
 *
 * @author Hunter
 */
public class FileOut {
     PrintStream fout; 
   
   FileOut(String filename){
     try{
       fout= new PrintStream ( new FileOutputStream(filename));
     }catch(IOException fo){
         System.out.println(fo); 
      }
    }

   public void writer(String out)
   {
     
         fout.println(out);
      
   }
   public void writer(int out)
   {
     
         fout.println(out);
      
   }
   public void writer(char out)
   {
     
         fout.println(out);
      
   }
   public void writer(double out)
   {
     
         fout.println(out);
      
   }
   public void writer(float out)
   {
     
         fout.println(out);
      
   }
/*following all write on one line*/

   public void write(String out)
   {
     
         fout.print(out);
      
   }

   public void write(int out)
   {
     
         fout.print(out);
      
   }

   public void write(char out)
   {
     
         fout.print(out);
      
   }

   public void write(float out)
   {
     
         fout.print(out);
      
   }

   public void write(double out)
   {
     
         fout.print(out);
      
   }


 
}
