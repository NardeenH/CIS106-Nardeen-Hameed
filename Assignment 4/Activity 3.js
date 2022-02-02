function main() {
    // Create a program that asks the user for a distance in miles, and then calculate and display the distance in yards, feet, and inches, or ask the user for a distance in miles, and then calculate and display the distance in kilometers, meters, and centimeters.
    var mile;
    var distanceFeet;
    var distanceYard;
    var distanceInches;
    var distanceKilometer;
    var distanceMeter;
    var distanceCentimeter;
    
    window.alert(" What is the Distance in Miles ? ");
    mile = window.prompt('Enter a value for mile');
    distanceFeet = mile * 5280;
    distanceYard = mile * 1760;
    distanceInches = mile * 63360;
    distanceKilometer = mile * 1.6069344;
    distanceMeter = mile * 1609.34;
    distanceCentimeter = mile * 160934;
    window.alert(" The distance in Feet is = " + distanceFeet);
    window.alert(" The distance in Yard is = " + distanceYard);
    window.alert(" The distance in Inches is = " + distanceInches);
    window.alert(" The distance in kilometer is = " + distanceKilometer);
    window.alert(" The distance in Meter is = " + distanceMeter);
    window.alert(" The distance in centimeter is = " + distanceCentimeter);
}
