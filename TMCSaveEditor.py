#def get_save_file(file_number):
    #input('file number 0 to 2') as file_number
    #if file_number < 0 or file_number > 2:
        #raise IndexError("File number must be either 0, 1, 2.")
    #return SaveFile(read_checksum(file_number), read_data(file_number))


def CalculateChecksum(filenumber : int) -> int:
    #print('filenumbuh: ',filenumber)
    gameState = data[0x34 + (filenumber * 0x10):0x34 + (filenumber * 0x10) + 0x04]
    gameData = data[0x80 + (filenumber * 0x500):0x80 + (filenumber * 0x500) + 0x500]
    shortcheck = partial_check(gameState)
    longcheck = partial_check(gameData)

    combined = (shortcheck + longcheck) & 0xFFFF
    upper = combined << 16
    lower = ~combined & 0xFFFF

    lower += 1
    combined = upper + lower
    return combined

def undo_reverse(data: bytes) -> bytes:
    data = bytearray(data)
    for i in range(0, len(data), 8):
        data[i:i + 8] = int.from_bytes(data[i:i + 8], 'big').to_bytes(8, 'little')
    return bytes(data)

def partial_check(data: bytes) -> int:
    pos = 0
    remaining = len(data)
    sum = 0
    while remaining > 0:
        sum += (data[pos] | (data[pos + 1] << 8)) ^ remaining
        pos += 2
        remaining -= 2
    sum &= 0xFFFF
    return sum

with open(input('Enter filename with extension: '), "r+b") as input_file:
    filenumber = int(input('Enter file number between 0 to 2: '))
    if filenumber < 0 or filenumber > 2:
        raise IndexError("File number must be either 0, 1, 2.")
    filename = input('Enter new file name: ')
    filenameSpace = 6 - len(filename)
    xtraSpace = filenameSpace * "0"
    input_file.seek(258 + (filenumber*1280))
    input_file.write(bytes([00,00,00,00,00,00]))
    input_file.seek(258 + (filenumber*1280))
    filenumbuh = filenumber
    if filenameSpace > 0:
        input_file.write(int(xtraSpace).to_bytes(filenameSpace, byteorder='little'))
    input_file.write(bytes(filename[::-1], 'ascii'))
    #brightness = int(input('Enter brightness between 0 to 2: '))
    #if brightness < 0 or brightness > 2:
    #    raise IndexError("Brightness must be either 0, 1, 2.")
    #input_file.seek(132 + (filenumbuh*1280))
    #input_file.write(brightness.to_bytes())
    Speed = int(input('Enter message speed between 0 to 2: '))
    if Speed < 0 or Speed > 2:
        raise IndexError("Message speed must be either 0, 1, 2.")
    input_file.seek(133 + (filenumbuh*1280))
    input_file.write(Speed.to_bytes())
    health = float(input('Enter the amount of health remaining: '))
    health *= 8
    if health < 0 or health > 160:
        raise IndexError("Health must be between 0 to maybe 160.")
    input_file.seek(301 + (filenumbuh*1280))
    input_file.write(int(health).to_bytes())
    #rupees = int(input('Enter amount of rupees: '))
    #input_file.seek(327 + (filenumbuh*1280))
    #input_file.write((rupees).to_bytes())
    #spawnPointyBig = int(input('Enter spawn point y big: '))
    #input_file.seek(264)
    #input_file.write((spawnPointyBig).to_bytes())
    #spawnPointySmall = int(input('Enter spawn point y small: '))
    #input_file.seek(265)
    #input_file.write((spawnPointySmall).to_bytes())
    #spawnPointxBig = int(input('Enter spawn point x big: '))
    #input_file.seek(266)
    #input_file.write((spawnPointxBig).to_bytes())
    #spawnPointxSmall = int(input('Enter spawn point x small: '))
    #input_file.seek(267)
    #input_file.write((spawnPointxSmall).to_bytes())
    #spawnAnim = int(input('Enter spawn animation: '))
    #input_file.seek(268)
    #input_file.write((spawnAnim).to_bytes())
    #room = int(input('Enter room of area to spawn in: '))
    #input_file.seek(270)
    #input_file.write((room).to_bytes())
    #area = int(input('Enter area to spawn in: '))
    #input_file.seek(271)
    #input_file.write((area).to_bytes())
    #Ezlo = int(input('Enter 8 for hatless or 38 for hat: '))
    #input_file.seek(729)
    #input_file.write((Ezlo).to_bytes())
    input_file.seek(0)
    data = input_file.read()
    data = undo_reverse(data)
    #print('Fire!!', filenumber)
    CalculateChecksum(filenumber)
    newchecksum = CalculateChecksum(filenumber)
    input_file.seek(48+(filenumbuh*16))
    input_file.write(((newchecksum & 4294901760) >> 16).to_bytes(8))
    input_file.seek(48+(filenumbuh*16))
    input_file.write((newchecksum & 0xFFFF).to_bytes(8))
    input_file.seek(54+(filenumbuh*16))
    big_byte = int.from_bytes(input_file.read(2))
    input_file.seek(52+(filenumbuh*16))
    input_file.write((65536-big_byte).to_bytes(2))
    input_file.seek(48+(filenumbuh*16))
    input_file.write(bytes([77, 67, 90, 51]))
    if filenumbuh == 0:
        input_file.seek(52)
        fourtofive=input_file.read(2)
        input_file.seek(54)
        sixtoseven=input_file.read(2)
        input_file.seek(52)
        input_file.write(sixtoseven)
        input_file.seek(54)
        input_file.write(fourtofive)
    elif filenumbuh == 1:
        input_file.seek(68)
        fourtofive=input_file.read(2)
        input_file.seek(70)
        sixtoseven=input_file.read(2)
        input_file.seek(68)
        input_file.write(sixtoseven)
        input_file.seek(70)
        input_file.write(fourtofive)
    elif filenumbuh == 2:
        input_file.seek(84)
        fourtofive=input_file.read(2)
        input_file.seek(86)
        sixtoseven=input_file.read(2)
        input_file.seek(84)
        input_file.write(sixtoseven)
        input_file.seek(86)
        input_file.write(fourtofive)
