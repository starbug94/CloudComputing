<%@ page contentType="text/html;charset=utf-8" import="java.sql.*" %>

	<%
 request.setCharacterEncoding("utf-8");  //Set encoding
 String id  =        request.getParameter("id");            
 String password =     request.getParameter("password");
 String name =   request.getParameter("name");
 String age = 		request.getParameter("age");
 String email  =   request.getParameter("email");

//POST로 Input.html로부터 입력받은 내용을 변수화

 try{
  Class.forName("com.mysql.jdbc.Driver");

  Connection con = DriverManager.getConnection("jdbc:mysql://192.168.56.102:3306/termtest", "root","2210109h");
  Statement stat = con.createStatement();

  String query = "INSERT INTO NewName(id, name, password, age, email)  VALUES('"+id+"','"+name+"','"+password+"','"+age+"','"+email+"')";
//INSERT into member(id,name,pwd,email) VALUES ('id','name','pwd','email') 쿼리문
  stat.executeUpdate(query);
  stat.close();
  con.close();
 }
 catch(Exception e){
  out.println( e );
 }
 response.sendRedirect("output.jsp"); 
	%>