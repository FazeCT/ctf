#!/usr/bin/python3
import angr
import claripy


def solver():
    print("""ANGR Solver by FazeCT, 1.0 edition.\nGithub: https://github.com/FazeCT
    """)
    source = input("Binary\'s Path (Ex: E:/Downloads/test.exe):")  # Get the binary's path
    mode = int(input("Solve with input constraints (1 if YES, 0 otherwise):"))  # Get solve mode
    assert mode in [0, 1], f"0 or 1 expected, got: {mode}"

    if mode == 1:
        length = int(input("Length of the input: ")) # Get input's length
        assert type(length) is int, f"integer expected, got: {type(length)}"
        assert length > 0, f"length greater than 0 expected, got: {length}"

        cons = int(input("Use printable constraints? (1 if YES, 0 otherwise): "))  # Printable enabled or disabled
        assert cons in [0, 1], f"0 or 1 expected, got: {cons}"

        win = input("Address to find (Ex: 0x08048B92): ")  # Get to-find address
        try:
            win = int(win, 16)
        except:
            print('Hex expected, abort now.')
            exit(0)

        lose = input("Address to avoid (Ex: 0x08048C88): ")  # Get to-avoid address
        try:
            lose = int(lose, 16)
        except:
            print('Hex expected, abort now.')
            exit(0)

        form = input("Known flag format? (Ex: picoctf{}) (Input -1 if trying to find non-flag inputs): ")

        opt = int(input("Add base address? (For PIE - enabled executables, 1 if YES, 0 otherwise): "))
        assert opt in [0, 1], f"0 or 1 expected, got: {opt}"

        p = angr.Project(source)
        inp = claripy.BVS("flag", length * 8)
        state = p.factory.entry_state(stdin=inp)

        if cons:
            for c in inp.chop(8):
                state.solver.add(c <= 0x7f)
                state.solver.add(c >= 0x20)

        if form != -1:
            try:
                for i in range(len(form) - 1):
                    state.solver.add(inp.chop(8)[i] == ord(form[i]))
                state.solver.add(inp.chop(8)[-1] == ord(form[-1]))
            except:
                print('Invalid format/length')
                exit(0)

        simgr = p.factory.simulation_manager(state)
        print("Solving...")
        simgr.explore(find=win + opt * 0x400000, avoid=lose + opt * 0x400000)

        try:
            res = simgr.found[0]
            print("Solution found!")
            for i in range(3):
                print(res.posix.dumps(i))
        except:
            print('No solution.')

    else:
        win = input("Address to find (Ex: 0x08048B92): ")  # Get to-find address
        try:
            win = int(win, 16)
        except:
            print('Hex expected, abort now.')
            exit(0)

        lose = input("Address to avoid (Ex: 0x08048C88): ")  # Get to-avoid address
        try:
            lose = int(lose, 16)
        except:
            print('Hex expected, abort now.')
            exit(0)

        opt = int(input("Add base address? (For PIE - enabled executables, 1 if YES, 0 otherwise): "))
        assert opt in [0, 1], f"0 or 1 expected, got: {opt}"

        p = angr.Project(source)
        state = p.factory.entry_state()

        simgr = p.factory.simulation_manager(state)
        print("Solving...")

        simgr.explore(find=win + opt * 0x400000, avoid=lose + opt * 0x400000)

        try:
            res = simgr.found[0]
            print("Solution found!")
            for i in range(3):
                print(res.posix.dumps(i))
        except:
            print('No solution.')


if __name__ == "__main__":
    solver()

