A = input("Room A: ").strip().upper()
B = input("Room B: ").strip().upper()
pos = input("Position (A/B): ").strip().upper()
rooms = {'A': A, 'B': B}
# Clean the current room if dirty
if rooms[pos] == "DIRTY":
    print("SUCK")
    rooms[pos] = "CLEAN"
# Find the other room
other = 'B' if pos == 'A' else 'A'
# Move to the other room and clean it if dirty
if rooms[other] == "DIRTY":
    print("MOVE RIGHT" if pos == 'A' else "MOVE LEFT")
    pos = other
    print("SUCK")
    rooms[pos] = "CLEAN"
print("Final State:", rooms)
