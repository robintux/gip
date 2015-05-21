def hanoi(disks,S,T,A):
    if disks == 1:
        print 'Move disk from',S,'to',T
        return
    hanoi(disks - 1, S, A, T)
    print 'Move disk from',S,'to',T
    hanoi(disks - 1, A, T, S)
    return

hanoi(3,'S','T','A')
