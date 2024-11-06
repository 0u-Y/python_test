from multiprocessing import Pool


def function(x):
    if x == 6:
        raise ValueError("6에서 오류가 발생")
    return x * x


if __name__ == "__main__":

    numbers = [1,2,3,4,5,6,7,8,9,10]

    print("map 사옹 결과")

    with Pool(processes=10) as pool:
        try:
            result = pool.map(function, numbers)
            print("결과: ", result)
        except ValueError as e:
            print(e)

    

    print("imap 사용 결과")
    with Pool(processes=10) as pool:
        results = pool.imap(function, numbers)
        try:
            for result in results:
                print("결과: ", result)
        except ValueError as e:
            print(e)



        

        
