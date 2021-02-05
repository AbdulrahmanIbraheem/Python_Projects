

print("*" * 80)
print("...welcome to check number of room(s) in a hotel...".center(80,"#"))
print("*" * 80)

print("\n\n")

keep_going = input("do you want to chack the number of room()s) (yes or no) ".capitalize() )
 


total_number_of_rooms = 0
total_number_of_rooms_used = 0


while  keep_going ==  "yes" or keep_going == "y":
  flord_number = int( input("\nEnter the number of floors in the hotel ").strip() )

  if flord_number < 1:

    print("error, the floors should not be less than 1".capitalize() )
    print("try again later".capitalize() )

    # break
    
    keep_going = input("do you want to chack the number of room()s) (yes or no) ".capitalize() )


  else:


    for floor in range(1,flord_number+1):

      print("---------------------------------------------------")
      print(f"floor number {floor}")
      number_of_rooms = int(input(f"enter the number of room(s) in floor number {floor} ".capitalize() ).strip())
  
      rooms_used = int( input(f"enter the number of room(s) are in used in floor number {floor} ".capitalize() ) )
      
      
      print(f"the number of room(s) in the floor {floor} are {number_of_rooms} room(s)".capitalize() )
      print(f"the number of room(s) are used in floor {floor} are {rooms_used} room(s)")

      total_number_of_rooms += number_of_rooms
      total_number_of_rooms_used += rooms_used

      prcentage_of_room_used = (total_number_of_rooms_used / total_number_of_rooms) * 100
    print("-------------------------------------------------------------------------------------")
    print(f"\nThe total number of room(s) in the hotel are {total_number_of_rooms}".capitalize() )
    print(f"the total number of room(s) used are {total_number_of_rooms_used}".capitalize() )
    print(f"The percentage of number of room(s) used are %{int(prcentage_of_room_used)} from the total room(s)")

    keep_going = input("do you want to rechack (yes or no) ".capitalize() )

    if not any([keep_going == "yes", keep_going == "y"]):
      break




