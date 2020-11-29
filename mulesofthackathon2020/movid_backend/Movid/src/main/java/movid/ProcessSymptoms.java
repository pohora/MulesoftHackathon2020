package movid;


public class ProcessSymptoms {
		
		
		public static String processSymptoms(String age,String gender,String lifeThreateningSymptoms,String feelingSick,String hasSymptoms,String liveInLongTermCareFacility,String lastTwoWeeksHealthCareFacility,String hasChronicCondition,String lastTwoWeeksPresenceCovidInfected) {
			
			String speak_output="";
			
			if(Integer.parseInt(age)<18) {
				//Pediatric Flow
				speak_output=speak_output+" You are under the age of 18. This requires the Pediatric Flow which is currently not supported. ";
			}else {
				//speak_output=speak_output+" You are older than 65";
				if(lifeThreateningSymptoms.contains("yes")) {
					return speak_output=CDCSymptomCheckerMessages.MSG4;
				}else {
					if(feelingSick.contains("yes")) {
						if(lastTwoWeeksPresenceCovidInfected.contains("yes")) {
                                if(hasSymptoms.contains("yes")) {
                                	
                                	      if(liveInLongTermCareFacility.contains("yes")) {
                                	    	           return CDCSymptomCheckerMessages.MSG7;
                                	      }else {//no and check if near healthcare facility
                                	    	         if(lastTwoWeeksHealthCareFacility.contains("yes")) {
                                	    	        	 
                                	    	        	 return CDCSymptomCheckerMessages.MSG9+CDCSymptomCheckerMessages.MSG6;
                                	    	        	 
                                	    	        	 
                                	    	         }else { // no , check for chronic health conditions
                                	    	        	        if(hasChronicCondition.contains("yes")) {
                                	    	        	        	    return CDCSymptomCheckerMessages.MSG5;
                                	    	        	        }else {
                                	    	        	        	    if(Integer.parseInt(age)>=65) {
                                	    	        	        	    	    return CDCSymptomCheckerMessages.MSG9;
                                	    	        	        	    }else {
                                	    	        	        	    	return CDCSymptomCheckerMessages.MSG8; 
                                	    	        	        	    }
                                	    	        	        }
                                	    	         }
                                	      }
                                	
                                	
								     //return speak_output="This is a generic assesment message";
							    }else { //no -> 
								return speak_output=CDCSymptomCheckerMessages.MSG10;
							}
							
						}else { //no
							if(hasSymptoms.contains("yes")) {
								 if(liveInLongTermCareFacility.contains("yes")) {
              	    	           return CDCSymptomCheckerMessages.MSG7;
              	      }else {//no and check if near healthcare facility
              	    	         if(lastTwoWeeksHealthCareFacility.contains("yes")) {
              	    	        	 
              	    	        	 return CDCSymptomCheckerMessages.MSG9+CDCSymptomCheckerMessages.MSG6;
              	    	        	 
              	    	        	 
              	    	         }else { // no , check for chronic health conditions
              	    	        	        if(hasChronicCondition.contains("yes")) {
              	    	        	        	    return CDCSymptomCheckerMessages.MSG5;
              	    	        	        }else {
              	    	        	        	    if(Integer.parseInt(age)>=65) {
              	    	        	        	    	    return CDCSymptomCheckerMessages.MSG9;
              	    	        	        	    }else {
              	    	        	        	    	return CDCSymptomCheckerMessages.MSG8; 
              	    	        	        	    }
              	    	        	        }
              	    	         }
              	      }
							}else { //no -> 
								return speak_output=CDCSymptomCheckerMessages.MSG10;
							}
						}
						
					}else { //not feeling sick -> ASYMPTOMATIC Flow
						
						if(lastTwoWeeksPresenceCovidInfected.contains("yes")) {
						 //return speak_output="This is a generic assesment message";
							if(liveInLongTermCareFacility.contains("yes")) {
								return CDCSymptomCheckerMessages.MSG7;
							}else { //no -check near healthcarefacility
								if(lastTwoWeeksHealthCareFacility.contains("yes")) {
									//TODO - ADD PPE CHECK
									return CDCSymptomCheckerMessages.MSG17+CDCSymptomCheckerMessages.MSG15;
								}else {
									return CDCSymptomCheckerMessages.MSG18;
								}
							}
						}else {
							return CDCSymptomCheckerMessages.MSG1;
						}
					}
				}
			}
			
			
			
			return speak_output;
		}

}



