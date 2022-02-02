function main() {
    // Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
    var hourly;
    var rate;
    var weekly;
    var yearly;
    var monthly;
    
    window.alert(" How many weekly hours did you work ?");
    hourly = window.prompt('Enter a value for hourly');
    window.alert(" What is your rate foy pay ?");
    rate = window.prompt('Enter a value for rate');
    weekly = rate * hourly;
    monthly = weekly * 4;
    yearly = weekly * 52;
    window.alert("Salary in Weekly: " + weekly);
    window.alert("Salary in Monthly: " + monthly);
    window.alert("Salary in Yearly: " + yearly);
}
