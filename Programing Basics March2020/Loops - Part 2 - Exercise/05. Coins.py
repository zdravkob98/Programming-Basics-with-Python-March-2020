coins = float(input())

count = 0
stotinki = round(coins * 100)
while stotinki > 0:
    if stotinki >= 200:
        stotinki -= 200
        count += 1
    elif stotinki >= 100:
        stotinki -= 100
        count += 1
    elif stotinki >= 50:
        stotinki -= 50
        count += 1
    elif stotinki >= 20:
        stotinki -= 20
        count += 1
    elif stotinki >= 10:
        stotinki -= 10
        count += 1
    elif stotinki >= 5:
        stotinki -= 5
        count += 1
    elif stotinki >= 2:
        stotinki -= 2
        count += 1
    elif stotinki >= 1:
        stotinki -= 1
        count += 1
print(count)
