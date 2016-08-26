/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hdms;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author koyexes
 */

public class Processes {
    private static int userId;
    private static String username;
    private static short priviledge;
    private static int numberOfMessagesInDatabase;
        
    public static Object [] verifyLoginInfo(String username, String password){
        try {
            try (Connection con = Methods.connectToDatabase()) {
                PreparedStatement pstmt = con.prepareStatement(SqlQueries.verifyUsernameAndPassword);
                pstmt.setString(1, username);
                pstmt.setString(2, password);
                ResultSet rs = pstmt.executeQuery();
                if(rs.next()){
                    PreparedStatement stmt = con.prepareStatement(SqlQueries.changeLoginStatus); // changing login status
                    stmt.setInt(1, 1);
                    stmt.setInt(2, rs.getInt("id"));
                    int rowAffected = stmt.executeUpdate();
                    if(rowAffected != 0){
                        return new Object[]{rs.getInt("id"),rs.getString("surname"),rs.getInt("priviledge")};
                    }else{
                        System.err.println("Couldn't change login status");
                        return null;
                    }
                }
            }
        } catch (Exception e) {
            Logger.getLogger(Processes.class.getName()).log(Level.SEVERE, null, e);
        }
        System.err.println("login failed");
        return null;
    }
    
    public static boolean logout(){
        try {
            try (Connection con = Methods.connectToDatabase()) {
                PreparedStatement stmt = con.prepareStatement(SqlQueries.changeLoginStatus); // changing login status
                stmt.setInt(1, 0);
                stmt.setInt(2, LoginPage.getUserId());
                int rowAffected = stmt.executeUpdate();
                if(rowAffected != 0){
                    return true;
                }
                  
            }
        } catch (Exception e) {
            Logger.getLogger(Processes.class.getName()).log(Level.SEVERE, null, e);
        }
        return false;
    }
    
   
}
