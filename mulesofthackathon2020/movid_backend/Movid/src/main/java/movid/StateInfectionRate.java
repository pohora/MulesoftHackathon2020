package movid;



public class StateInfectionRate {
	
	
	public static String stateInfectionRate(float infectionRate) {
		
		
		//round infection rate to 2 decimal places ie 1.05604540744 -> 1.06
		double roundedInfectionRate = Math.round(infectionRate * 100.0) / 100.0;
		
		
		String speach_output="The current infection rate is "+Double.toString(roundedInfectionRate)+" which is ";
		
		if(roundedInfectionRate<=0.9) {
			speach_output=speach_output+"Low. ";
		}else {
			if(roundedInfectionRate<=1.1) {
				speach_output=speach_output+"Medium. ";
				speach_output=speach_output+"Because this number is around 1.0, it means that COVID continues to spread, but in a slow and controlled fashion. ";
			}else {
				if(roundedInfectionRate<=1.4) {
					speach_output=speach_output+"High. ";
					speach_output=speach_output+"As such, the total number of active cases is growing at an unsustainable rate. If this trend continues, the hospital system may become overloaded. Caution is warranted. ";
				}else {
					if(roundedInfectionRate<=2.1) {
						speach_output=speach_output+"Critical. ";
						
					}
				}
			}
		}
		
		speach_output=speach_output+"On average,each person with COVID is infecting "+Double.toString(roundedInfectionRate)+" other people. ";
		
		
		
		
		return speach_output;
	}

}
