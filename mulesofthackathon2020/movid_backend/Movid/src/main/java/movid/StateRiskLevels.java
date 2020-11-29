package movid;

public class StateRiskLevels {
	//API Docs https://apidocs.covidactnow.org/api#tag/RiskLevels
	
	public static String stateRiskLevels(int overall,int infectionRate,int icuHeadroomRatio,int testPositivityRatio) {
		
		String speach_output="Risk level summary. ";
		switch(overall) {
		case 0:
			speach_output=speach_output+" Overall Risk Levels are Low and on track to contain COVID. ";
			break;
		case 1:
			speach_output=speach_output+" Overall Risk Levels are Medium with slow disease growth. ";
			break;
		case 2:
			speach_output=speach_output+" Overall Risk Levels are High, and at a risk of outbreak. ";
			break;
		case 3:	
			speach_output=speach_output+" Overall Risk Levels are Critical, with an active or imminent outbreak. ";
			break;
		case 4:
			speach_output=speach_output+" Overall Risk Levels are unknown. ";
            break; 
		default:
			speach_output=speach_output+"Overall Risk Levels are unknown.";
		}
		
		
		switch(infectionRate) {
		case 0:
			speach_output=speach_output+" Infection Rate Risk levels are Low. ";
			break;
		case 1:
			speach_output=speach_output+" Infection Rate Risk levels are Slowy growing. ";
			break;
		case 2:
			speach_output=speach_output+" Infection Rate Risk levels are High. ";
			break;
		case 3:	
			speach_output=speach_output+" Infection Rate Risk levels are Critical. ";
			break;
		case 4:
			speach_output=speach_output+" Infection Rate Risk levels are unknown. ";
            break; 
		default:
			speach_output=speach_output+"Infection Rate Risk levels are unknown.";
		}
		
		switch(icuHeadroomRatio) {
		case 0:
			speach_output=speach_output+" ICU Headroom Ratio Risk levels are Low. ";
			break;
		case 1:
			speach_output=speach_output+" ICU Headroom Ratio Risk levels are Slowy growing. ";
			break;
		case 2:
			speach_output=speach_output+" ICU Headroom Ratio Risk levels are High. ";
			break;
		case 3:	
			speach_output=speach_output+" ICU Headroom Ratio Risk levels are Critical. ";
			break;
		case 4:
			speach_output=speach_output+" ICU Headroom Ratio Risk levels are unknown. ";
            break; 
		default:
			speach_output=speach_output+"ICU Headroom Ratio Risk levels are unknown.";
		}
		switch(testPositivityRatio) {
		case 0:
			speach_output=speach_output+" Test Positivity Risk levels are Low. ";
			break;
		case 1:
			speach_output=speach_output+" Test Positivity Risk levels are Slowy growing. ";
			break;
		case 2:
			speach_output=speach_output+" Test Positivity Risk levels are High. ";
			break;
		case 3:	
			speach_output=speach_output+" Test Positivity Risk levels are Critical. ";
			break;
		case 4:
			speach_output=speach_output+" Test Positivity Risk levels are unknown. ";
            break; 
		default:
			speach_output=speach_output+" Test Positivity Risk levels are unknown. ";
		}
		
		
		
		return speach_output;
	}

}
