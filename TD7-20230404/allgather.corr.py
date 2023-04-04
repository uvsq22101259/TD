#!/usr/bin/python3

import argparse
import multiprocessing as mp
import os
import sys

import agutils

def send_message(pipe_out):
    """
    Fonction utilisée par les processus fils pour envoyer un message au
    processus principal.
    Message constitué de 2 parties :
        - un identifiant généré par agutils.createID(),
        - un message généré par agutils.createMessage()

    Entrée : pipe_out -- tube de communication en écriture
    """

    with os.fdopen(pipe_out, "w") as f:
        mid = agutils.createID()
        msg = agutils.createMessage()
        print("I(%d) chose %s!" % (mid, msg))
        f.write("%d\n%s\n" % (mid, msg))

def allgather(pipe_in, num_process):
    """
    Fonction utilisée par le processus principal pour récupérer l'ensemble des
    messages des processus fils, aggrégé dans un dictionnaire {id: msg}.
    Entrée : pipe_in -- tube de communication en lecture
             num_process -- nombre de processus fils
    Sortie : dictionnaire {id: msg} des informations récupérées du tube
    """

    res = {}
    with os.fdopen(pipe_in) as f:
        for _ in range(num_process):
            i = int(f.readline()[:-1])
            res[i] = f.readline()[:-1]

    return res

if __name__ == '__main__':
    """
    Fonction principale : a pour but de créer args.np processus appelant
    send_message() pour transmettre des informations au processus principal qui
    les récupère à l'aide de allgather().
    """

    # DO NOT MODIFY THE ARGPARSE PART
    AP = argparse.ArgumentParser()
    AP.add_argument('np', help='number of processes', type=int)
    args = AP.parse_args(sys.argv[1::])

    # START IMPLEMENT MAIN HERE
    r, w = os.pipe()
    process_list = []
    for i in range(args.np):
        process_list.append(mp.Process(target=send_message, args=[w]))

    for p in process_list:
        p.start()

    os.close(w)
    res = allgather(r, args.np)

    for i, s in res.items():
        print("%d chose '%s'." % (i, s))

    for p in process_list:
        p.join()