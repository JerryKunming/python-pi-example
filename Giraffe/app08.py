month_conversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(month_conversions["Apr"])
print(month_conversions["Nov"])
print(month_conversions.get("Jan", "Not a valid key"))
print(month_conversions.get("NNN", "Not a valid key"))

