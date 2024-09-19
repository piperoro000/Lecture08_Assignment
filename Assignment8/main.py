from seqbio.SeqMan.dnaconvert import reverseComplementSeq,transcription,translation
from seqbio.calculation.SeqCal import gcContent,countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan
import re
def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action='store_true', default=None,
                             help="Convet DNA to reverse-complementary")

    d2r_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    d2r_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    d2r_command.add_argument("-r", "--revcomp", action='store_true', default=None,
                             help="Convet DNA to reverse-complementary")
    
    d2p_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    d2p_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    d2p_command.add_argument("-r", "--revcomp", action='store_true', default=None,
                             help="Convet DNA to reverse-complementary")
    
    enzserch_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzserch_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    enzserch_command.add_argument("-r", "--revcomp", action='store_true', default=None,
                             help="Convet DNA to reverse-complementary")  

    # parser.print_help()
    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()
    
    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        elif args.revcomp:
            print("Input",args.seq,"\ncountBases =", countBasesDict(reverseComplementSeq(seq)) )
        else:
            print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        elif args.revcomp:
            print("Input",args.seq,"\ntranscription =", transcription(reverseComplementSeq(seq)) )
        else:
            print("Input",args.seq,"\ntranscription =", transcription(seq) )

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        elif args.revcomp:
            print("Input",args.seq,"\ntranscription =", translation(reverseComplementSeq(seq)) )
        else:
            print("Input",args.seq,"\ntranslation =", translation(seq) )
    
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        elif args.revcomp:
            print(f"Input {args.seq}\n{args.enz} site = {enzTargetsScan(reverseComplementSeq(seq), args.enz)}")
        else:
            print(f"Input {args.seq}\n{args.enz} site = {enzTargetsScan(seq, args.enz)}")


if __name__ == "__main__":
    main()
