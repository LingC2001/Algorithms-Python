import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from suffix_array import SuffixArray
import time

def check_sorted(sa):
    for i in range(len(sa.suffix_arr)-1):
        if sa.string[sa.suffix_arr[i]:] > sa.string[sa.suffix_arr[i+1]:]:
            print(f'{sa.string[sa.suffix_arr[i]:]} >  {sa.string[sa.suffix_arr[i+1]:]}')
            return False
    return True

def test_construction_time():
    
    start_t = time.time()
    sa = SuffixArray("MISSISSIPPI")
    print(f'Time taken: {time.time()-start_t}')
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)
    
    start_t = time.time()
    sa = SuffixArray("CAMEL")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("BANANA")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("jkasdhfoiweAJKSHDiawebiweIASDHIWQu")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)
    
    start_t = time.time()
    sa = SuffixArray("JKLAHSFIJNEIOUFHWIOUHEFOIWEFHIDNSVJKSDVIOUEHWOIUFRHEUIWHFSKDJHFIOEWUHFIODBVO*WI")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)
    
    start_t = time.time()
    sa = SuffixArray("AAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAA")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("AAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDD")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)
    
    start_t = time.time()
    sa = SuffixArray("CNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWI")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    for i in range(len(sa.suffix_arr)-1):
        assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("CNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWInweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWINWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWIfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWI")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    # for i in range(len(sa.suffix_arr)-1):
    #     assert check_sorted(sa)

    start_t = time.time()
    sa = SuffixArray("CNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWInweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWINWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWIfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWICNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWInweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWINWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrCNUIOEWIEUEWUIUIUIFHUIWEUHFUFHUFHEOWIVNWNEUIIoiUBWEOFGWEOUYFOIUEFHNWEiuvhoiweubocinIOBEOUIFCNOIWEUVbiosdvoEIUVSDJvwoieuvbdsjbvouBOUIEBVOUIbwoevbksdvhboaiwbiubAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAAAAAAAAAAABBBBBBBBAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBBBBAAACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDJKLHjklfhwioeneovinweoeiurhterovnweijrfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWIfnvuoweiurgtghwoolsajlkdfhwoiquefOIHIUWOIUgoquiwehfdOIUHBOIBEWIUFHOWI")
    print(f'Time taken: {time.time()-start_t}')
    # sa.print_suffixes()
    # for i in range(len(sa.suffix_arr)-1):
    #     assert check_sorted(sa)
