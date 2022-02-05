from browser import document,console,alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']
def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    match x:
        case'Kijang Inova':
            return y * 500000
        case'Avanza':
            return y * 450000
        case'Jazz':
            return y * 350000
        case'Brio':
            return y * 300000
        case'Luxio':
            return y * 300000
        case'Xenia':
            return y * 250000
        
def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)

