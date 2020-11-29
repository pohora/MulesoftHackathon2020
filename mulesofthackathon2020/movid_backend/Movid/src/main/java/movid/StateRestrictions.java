package movid;

public class StateRestrictions {
	
	
	public static String determineStateRestrictions(String Gathering_Restriction_Code,String School_Closure_Code,String Non_Essential_Business_Closure_Code,String Social_Distancing_Requirement_Code,String Face_Covering_Policy_Code,String Bar_Restrictions_Code,String Reopening_Plan_Code,String Stay_at_Home_Requirement_Code,String Domestic_Travel_Restrictions_Code,String Restaurant_Restrictions_Code) {
		
		String speach_output="";
		if(Gathering_Restriction_Code!=null) {
			speach_output=speach_output+"Gathering Restrictions are currently: "+Gathering_Restriction_Code+". ";
		}
		if(School_Closure_Code!=null) {
			speach_output=speach_output+"School Closures are currently: "+School_Closure_Code+". ";
		}
		if(Non_Essential_Business_Closure_Code!=null) {
			speach_output=speach_output+"Non essential businesses are currently: "+Non_Essential_Business_Closure_Code+". ";
		}
		if(Social_Distancing_Requirement_Code!=null) {
			speach_output=speach_output+"Social Distancing requirements are currently: "+Social_Distancing_Requirement_Code+". ";
		}
		
		
		if(Face_Covering_Policy_Code!=null) {
			speach_output=speach_output+"Face Covering Policy is currently: "+Face_Covering_Policy_Code+". ";
		}
		if(Bar_Restrictions_Code!=null) {
			speach_output=speach_output+"Bar Restrictions are currently: "+Bar_Restrictions_Code+". ";
		}
		if(Reopening_Plan_Code!=null) {
			speach_output=speach_output+"Reopening Plans are currently: "+Reopening_Plan_Code+". ";
		}
		if(Stay_at_Home_Requirement_Code!=null) {
			speach_output=speach_output+"The Stay at Home requirement is currently: "+Stay_at_Home_Requirement_Code+". ";
		}
		if((Domestic_Travel_Restrictions_Code!=null) && (!Domestic_Travel_Restrictions_Code.contains("-"))) {
			speach_output=speach_output+"The Domestic Travel restriction is currently: "+Domestic_Travel_Restrictions_Code+". ";
		}
		if(Restaurant_Restrictions_Code!=null) {
			speach_output=speach_output+"The Restaurant restriction requirement is currently: "+Restaurant_Restrictions_Code+". ";
		}
		
		
		
		
		return speach_output;
	}

}
