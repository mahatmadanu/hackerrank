def catAndMouse(x, y, z)
    # Complete this function
    catchMouse = []
    mouse1 = x-z
    mouse2 = y-z
    mouse1 = mouse1.abs
    mouse2 = mouse2.abs
    if mouse1 < mouse2
        puts "Cat A"
    elsif mouse1 > mouse2
        puts "Cat B"
    else
        puts "Mouse C"
    end
    
end