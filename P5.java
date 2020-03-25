import java.util.Calendar;
class Solution {
  public String solution(int a, int b) {
      Calendar cal = Calendar.getInstance();
      String answer="";
      String [] res={"MON","TUE","WED","THU","FRI","SAT","SUN"};
      cal.set(2016,a-1,b-1);
      answer =res[cal.getTime().getDay()];
      return answer;
  }
}
