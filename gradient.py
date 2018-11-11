# conding:utf-8
rooms = [3, 3, 3, 2, 4]
price = [400, 330, 369, 232, 540]
area = [2104, 1600, 2400, 1416, 3000]


def gradientDescent(rooms, price, area):
    theta = [1, 1, 1]
    iteras = 400
    i = 1
    temp0, temp1, temp2 = theta[0], theta[1], theta[2]
    while i <= iteras:
        print "iteras=:"+str(i)
        sum0 = 0
        sum1 = 0
        sum2 = 0
        # for theta0
        for m in range(len(rooms)):
            h_theta = theta[0] + theta[1] * area[m] + theta[2] * rooms[m]
            y_m = price[m]
            sum0 += (h_theta - y_m) * 1
        # for theta1
        for m in range(len(rooms)):
            h_theta=theta[0]+theta[1]*area[m]+theta[2]*rooms[m]
            y_m=price[m]
            sum1+=(h_theta-y_m)*area[m]
        # for theta2
        for m in range(len(rooms)):
            h_theta = theta[0] + theta[1] * area[m] + theta[2] * rooms[m]
            y_m = price[m]
            sum2+=(h_theta-y_m)*rooms[m]

        temp0 -= 0.0000001 * 0.2 * sum0
        temp1 -= 0.0000001 * 0.2 * sum1
        temp2 -= 0.0000001 * 0.2 * sum2

        if abs(temp0 - theta[0]) <= 0.0001 and abs(temp1 - theta[1]) <= 0.0001 and abs(temp2 - theta[2]) <= 0.0001:
            break

        theta[0] = temp0
        theta[1] = temp1
        theta[2] = temp2
        i += 1
    return theta


theta_result = gradientDescent(rooms, price, area)
print(theta_result)

predict = theta_result[0] + theta_result[1] * 2104 + theta_result[2] * 3
# print(predict)
