/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hdms;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.UIManager;

/**
 *
 * @author koya
 */
public class Methods{
   
  private static Connection con;
   
   // resetting gridbagconstraints values
   
    
    static void lookAndFeel(){
       try {
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (Exception e) {
        }

    }
    
    
    static Connection connectToDatabase()throws SQLException{      
       con = DriverManager.getConnection("jdbc:mysql://localhost:3306/hdms", "root", ""); 
       return con;    
    }
    
      
    static String toCamelCase(String string){
        try{
            String name = string.toUpperCase();
            StringBuilder camelCasedString = new StringBuilder();
            String [] splitedName = name.split(" ");
            for (String splitedName1 : splitedName) {
                String lowerName = splitedName1.toLowerCase();
                String camelName = null;
                if((lowerName.substring(0, 1)).matches("[a-zA-z]")){
                    camelName = lowerName.replaceFirst(lowerName.substring(0, 1), splitedName1.substring(0, 1));
                    camelCasedString.append(camelName).append(" ");           
                }else{
                    int x = 0;
                    while((lowerName.substring(x, x+1)).matches("[a-zA-z]") == false){
                        x++;
                    }
                    camelName = lowerName.replaceFirst(lowerName.substring(x, x+1), splitedName1.substring(x, x+1));
                    camelCasedString.append(camelName).append(" ");     
                }


            }
            return camelCasedString.toString();
        }catch(Exception e){
            return string;
        }
            
    }
    
   
  
    
   
}
