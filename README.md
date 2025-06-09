# Fire Weather Index (FWI) Predictor using Machine Learning

This project uses real environmental data (from June to September 2012) to predict Fire Weather Index and determine fire occurrence likelihood. Built using Python and Simple Linear Regression.

## Features
- Inputs: Temperature, Relative Humidity, Wind Speed, Rainfall
- Outputs: FWI value + Fire classification
- FWI Components predicted: FFMC, DMC, DC, ISI, BUI
- Model: Simple Linear Regression
- Tools: pandas, scikit-learn, matplotlib

## Dataset Fields
- `Temp`: 22–42°C  
- `RH`: 21–90%  
- `Ws`: 6–29 km/h  
- `Rain`: 0–16.8 mm  
- `FWI`: 0–31.1  
- `Classes`: Fire / No Fire

## Goal
To build an AI model that can assist in forest fire risk analysis and environmental monitoring.

---

Made with ❤️ using Python
