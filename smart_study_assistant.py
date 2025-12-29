print("📘 Welcome to AI Smart Study Assistant")

subject = input("Enter subject name: ")
hours = int(input("Enter study hours available today: "))
level = input("Are you weak in this subject? (yes/no): ").lower()

print("\n🧠 AI Study Plan for", subject)

if hours <= 1:
    print("- Revise key concepts")
    print("- Read short notes")

elif hours == 2:
    print("- 1 hour theory")
    print("- 1 hour practice")

else:
    print("- 1 hour theory")
    print("- 1 hour practice")
    print("- 1 hour revision")

# Performance-based intelligence
if level == "yes":
    print("⚠️ Focus more on basics and revise twice.")
else:
    print("✅ Try solving medium-level questions today.")

# Motivation tip
print("\n✨ AI Motivation Tip:")
print("Consistency is more important than studying long hours once.")
