def calc_square_root(n):
    # write code that generates an error
    try:
        from my_math_calculator import sqrt
    except ModuleNotFoundError:
        from Math import sqrt
        print("My_math_calculator module not available. Using default.")

    from warnings import warn
    warn("You are runing a not so good function.")

    try:
        answer = sqrt(n)
    except TypeError:
        print("Enter something different")
    except ValueError:
        print("Do not enter a negative number")
    except Exception:
        print("Exception")
    else:
        return answer


def main():
    calc_square_root(4)


if __name__ == "__main__":
    main()
