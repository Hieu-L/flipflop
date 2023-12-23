import sys, getopt


# =======================[ READ FILE ]=======================

def read_file(filename) :
    """ 
    an paranoid way to read a file \n\n
    Returns args , atks \n
    args : a list of all arguments, which are represented as Strings \n
    atks : a list of tuple of arguments, which are represented as Tuples of Strings 
    """
    args = []
    atks = []

    with open(filename,'r') as f :
        lines = f.readlines()
        
        for l in lines :
            
            # READ ARGUMENTS
            if "arg" in l :
                a = "" ; skip = "arg("
                for i in range(len(l)) :
                    if skip != "" :
                        skip = skip[1:]
                    elif (skip=="") and (l[i]!=')') :
                        a = a + l[i]
                    if l[i] == ')' :
                        break
                args.append(a)

            # READ ATTACKS
            elif "att" in l :
                atk = "" ; dfn = ""
                skip = "att(" ; switch = True
                for i in range(len(l)) :
                    # shameful pls look away
                    if skip != "" :
                        skip = skip[1:]    
                        continue
                    if l[i] == ',' :
                        switch = False     
                        continue
                    if l[i] == ')' :
                        break
                    if (skip=="") and switch :
                        atk = atk + l[i]                    
                    if (skip=="") and not switch :
                        dfn = dfn + l[i]              
                atks.append( (atk,dfn) )

    return args , atks      

# ==================[ IS ADMISSIBLE CHECK ]==================

# done
def conflict_free(argset,atks) :
    """
    Return True or False \n
    argset : a list of arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n\n
    checks if 'argset' is conflict free.
    """
    
    for s in argset :
        for a,d in atks :
            # if 's' attacks an argument within the set
            if (s==a) and (d in argset) : 
                return False
    
    return True

# done
def self_defense(argset,atks) :
    """
    Return True or False \n
    argset : a list of arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n\n
    checks if 'argset' has the self-defense property.
    """

    for s in argset :
        for a,d in atks :
            # if 's' is attacked by a state 'a' ...
            if s == d :
                self_defended = False

                # ... try to find an argument in 'argset' that attacks 'a ...
                for ap,dp in atks :
                    if (dp == a) and (ap in argset) :
                        self_defended = True
                        break
                
                # ... and if you can't , argset is not self defensive
                if not self_defended :
                    return False
                
    
    return True

# ===================[ COMPLETE PROBLEMS ]===================

# done
def ve_co(args, atks, argset) :
    """
    Return True or False \n\n
    args : a list of arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n
    argset : a list of all arguments \n\n
    checks if 'argset' is a complete extension of F.
    """

    # check if 'argset' is admissible 
    if conflict_free(argset,atks) and self_defense(argset,atks) :
        
        # check 'argset' is complete
        for arg in args :
            
            all_defended = True
            
            for a,d in atks :

                # if arg is attacked ...
                if arg == d :

                    has_defender = False
                    
                    for ap,dp in atks :
                        # ... and the attacker is attacked by an argument in 'argset'
                        if (dp == a) and (ap in argset) : 
                            has_defender = True 
                            break
                    
                    if not has_defender :
                        all_defended = False
                        break
            
            if all_defended :
                if not (arg in argset) :
                    return False
        
        return True

    # if not admissible
    else :
        return False


def dc_co(args, atks, s) :
    """
    [ Return True or False | and | print "YES"/"NO" ] \n\n
    args : a list of all arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n
    s : an argument within args \n\n
    checks if s belongs to some complete extension of F.
    """
    ...


def ds_co(args, atks, s) :
    """
    [ Return True or False | and | print "YES"/"NO" ] \n\n
    args : a list of all arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n
    s : an argument within args \n\n
    checks if s belongs to each complete extension of F.
    """
    ...

# ====================[ STABLE PROBLEMS ]====================

def ve_st(args, atks, s) :
    """
    Return True or False \n\n
    argset : a list of arguments \n
    args : a list of all arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n\n
    checks if 'argset' is a stable extension of F.
    """
    ...


def dc_st(args, atks, s) :
    """
    [ Return True or False | and | print "YES"/"NO" ] \n\n
    args : a list of all arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n
    s : an argument within args \n\n
    checks if s belongs to some stable extension of F.
    """
    ...


def ds_st(args, atks, s) :
    """
    [ Return True or False | and | print "YES"/"NO" ] \n\n
    args : a list of all arguments | ex : [ 'A' , 'B' ] \n
    atks : a list of tuples of arguments, representing attacks | ex: [ ('Atk1','Def1') , ('Atk2','Def2') ] \n
    s : an argument within args \n\n
    checks if s belongs to each stable extension of F.
    """
    ...


# ==========================[ MAIN ]=========================

def main(argv):

    # receive input , split into filename, problem, and argument(s)
    opts , args = getopt.getopt(argv,"p:f:a:")

    filename = "" 
    problem = ""
    arguments = []

    for o,i in opts :
        if o == "-p" :
            problem = i
        elif o == "-f" :
            filename = i
        elif o == "-a" :
            arguments = i


    # read file
    all_args , atks = read_file(filename)


    # match problem to corresponding function

    match problem :

        # COMPLETE
        case "VE-CO" :
            arguments = arguments.split(',')
            if ve_co(all_args , atks , arguments) :
                print("YES")
            else :
                print("NO")

        case "DC-CO" :
            dc_co(all_args,atks,arguments)

        case "DS-CO" :
            ds_co(all_args,atks,arguments)
        

        # STABLE
        case "VE-ST" :
            arguments = arguments.split(',')
            if ve_st(all_args , atks , arguments) :
                print("YES")
            else :
                print("NO")
        
        case "DC-ST" :
            dc_st(all_args,atks,arguments)
        
        case "DS-ST" :
            ds_st(all_args,atks,arguments)




if __name__ == "__main__":
   main(sys.argv[1:])