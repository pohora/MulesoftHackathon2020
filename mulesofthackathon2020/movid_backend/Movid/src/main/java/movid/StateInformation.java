package movid;

public class StateInformation {
	
	
	public static String provideStateInformation(String state,int population,int testPositivityRatio,float tpInfectionRate,int overallRiskLevel,int riskLeveltestPositivityRatio,int caseDensity,int contactTracerCapacityRatio,int infectionRate,int icuHeadroomRatio,int actualCases,int actualDeaths,int actualPositiveTests,int actualNegativeTests,int actualContactTracers,int hospitalBedCapacity,int newCases) {
		
		
		String speach_output="Today ";
		
		
		if(newCases>0) {
			speach_output=speach_output+"The number of new cases is "+ Integer.toString(newCases) +". ";
		}else {
			speach_output=speach_output+" ";
		}
		if(actualCases>0) {
			speach_output=speach_output+"The standing total number of confirmed or suspected cases is "+ Integer.toString(actualCases) +". ";
		}else {
			speach_output=speach_output+" ";
		}
		if(actualPositiveTests>0) {
			speach_output=speach_output+"The number of Positive tests to date is "+ Integer.toString(actualPositiveTests) +". ";
		}else {
			speach_output=speach_output+" ";
		}
		if(actualNegativeTests>0) {
			speach_output=speach_output+"The number of Negative tests to date is "+ Integer.toString(actualNegativeTests) +". ";
		}else {
			speach_output=speach_output+" ";
		}
		
		
		
		return speach_output;
	}

}
