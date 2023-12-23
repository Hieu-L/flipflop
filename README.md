All the code is contained in program.py

Content of program.py :

-  main()

[ INPUT / OUTPUT ]
-  read_file( filename : str ) -> List[str] , List[(str,str)] 

[ ADMISSIBILITY ] 
-  conflict_free( argset : List[str] , atks : List[(str,str)] ) -> Bool
-  self_defense( argset : List[str] , atks : List[(str,str)] ) -> Bool

For these functions below, F = < args , atks > is the argumentation framework.

[ COMPLETE PROBLEMS ]
- ve_co(args : List[str] , atks : List[(str,str)] , argset : List[str]) -> Bool
- dc_co(args : List[str] , atks : List[(str,str)] , argset) -> Bool
- ds_co(args : List[str] , atks : List[(str,str)] , argset) -> Bool

[ STABLE PROBLEMS ]
- ve_st(args : List[str] , atks : List[(str,str)] , argset : List[str]) -> Bool
- dc_st(args : List[str] , atks : List[(str,str)] , argset : List[str]) -> Bool
- ds_st(args : List[str] , atks : List[(str,str)] , argset : List[str]) -> Bool 
