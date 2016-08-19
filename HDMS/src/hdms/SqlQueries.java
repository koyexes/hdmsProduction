/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hdms;

/**
 *
 * @author koyexes
 */
public class SqlQueries {
    public static String verifyUsernameAndPassword = "SELECT * FROM users WHERE username = ? AND password = SHA1(?) ";
    public static String changeLoginStatus = "UPDATE users SET login_status = ? WHERE id = ? LIMIT 1 ";
}
