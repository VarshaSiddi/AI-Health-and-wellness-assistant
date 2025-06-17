# AI Health & Wellness Assistant
# Created by Varsha Siddi - June 2025

def get_input(prompt, cast_func=float):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def heart_rate_advice(hr):
    if 60 <= hr <= 100:
        return "Normal ❤️", 2
    elif hr < 60:
        return "Low 💙 - Consider light activity", 1
    else:
        return "High ❤️‍🔥 - Reduce stress & caffeine", 0

def bp_advice(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal 💓", 2
    elif 120 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "Elevated ⚠️ - Reduce salt intake", 1
    else:
        return "High 💢 - Consult a doctor", 0

def spo2_advice(spo2):
    if spo2 >= 95:
        return "Good 💨", 2
    elif 90 <= spo2 < 95:
        return "Mildly low 😮‍💨 - Deep breathing recommended", 1
    else:
        return "Low 😷 - Seek medical help", 0

def sugar_advice(sugar):
    if 70 <= sugar <= 140:
        return "Normal 🍬", 2
    elif sugar < 70:
        return "Low 🍭 - Have something sweet", 1
    else:
        return "High 🍩 - Avoid sugary food", 0

def temperature_advice(temp):
    if 97 <= temp <= 99:
        return "Normal 🌡️", 2
    elif temp < 97:
        return "Low 🥶 - Stay warm", 1
    else:
        return "High 🤒 - Take rest & stay hydrated", 0

def lifestyle_advice(score):
    print("\n🔹 Lifestyle Advice:")
    if score <= 5:
        print("• Focus on proper sleep 🛏️")
        print("• Stay hydrated 💧")
        print("• Eat more fruits & veggies 🥦🍎")
        print("• Exercise daily for 20–30 mins 🏃‍♀️")
    elif 6 <= score <= 8:
        print("• You're doing okay, but maintain balance ⚖️")
        print("• Reduce junk food & manage screen time 📱")
    else:
        print("• Great job! Keep up your healthy routine 💪")

def main():
    print("Welcome to the AI Health & Wellness Assistant 🤖")
    name = input("Enter your name: ")
    age = get_input("Enter your age: ", int)

    print(f"\nHi {name}, let's check your vitals 👩‍⚕️")

    hr = get_input("Enter your heart rate (bpm): ")
    bp_sys = get_input("Enter your systolic BP: ")
    bp_dia = get_input("Enter your diastolic BP: ")
    spo2 = get_input("Enter your SpO2 (%): ")
    sugar = get_input("Enter your blood sugar level (mg/dL): ")
    temp = get_input("Enter your body temperature (°F): ")

    print("\n📊 Health Report:")
    total_score = 0

    hr_status, hr_score = heart_rate_advice(hr)
    print(f"• Heart Rate: {hr_status}")
    total_score += hr_score

    bp_status, bp_score = bp_advice(bp_sys, bp_dia)
    print(f"• Blood Pressure: {bp_status}")
    total_score += bp_score

    spo2_status, spo2_score = spo2_advice(spo2)
    print(f"• SpO2: {spo2_status}")
    total_score += spo2_score

    sugar_status, sugar_score = sugar_advice(sugar)
    print(f"• Sugar: {sugar_status}")
    total_score += sugar_score

    temp_status, temp_score = temperature_advice(temp)
    print(f"• Temperature: {temp_status}")
    total_score += temp_score

    print(f"\n🧮 Total Health Score: {total_score}/10")
    lifestyle_advice(total_score)

    print("\nThanks for using the assistant, stay healthy! 🌿")

if __name__ == "__main__":
    main()
