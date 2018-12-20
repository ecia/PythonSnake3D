import bge
from random import random
def main():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    own['Delay']= (own['Delay']+1)%16
    
    sce= bge.logic.getCurrentScene()
    ob= sce.objects
    
    key=bge.logic.keyboard
    if own['Block']==False:
        if key.events[bge.events.UPARROWKEY]>0:
            own['Block']=True
            if own['X']!=0:
                own['X']=0
                own['Y']=1
        if key.events[bge.events.DOWNARROWKEY]>0:
            own['Block']=True
            if own['X']!=0:
                own['X']=0
                own['Y']=-1
        if key.events[bge.events.RIGHTARROWKEY]>0:
            own['Block']=True
            if own['Y']!=0:
                own['X']=1
                own['Y']=0
        if key.events[bge.events.LEFTARROWKEY]>0:
            own['Block']=True
            if own['Y']!=0:
                own['X']=-1
                own['Y']=0
                
    if key.events[bge.events.SPACEKEY]>0:
            own['Z']=1
                
                
    if 'Tails' not in own:
        own['Tails']=[sce.addObject('Tail')]
    
    if own['Delay']==0: 
        own['Block']=False
        for i in range( len( own['Tails'] ) -1, -1, -1):
            own['Tails'][i].worldPosition= own['Tails'][i-1].worldPosition
        
        
        own['Tails'][0].worldPosition= own.worldPosition
        
        
        own.worldPosition[0]+=own['X']
        own.worldPosition[1]+=own['Y']
        own.worldPosition[2]+=own['Z']
        own['Z']=0
        
        if      own.worldPosition[0]== ob['Food'].worldPosition[0]:
            if  own.worldPosition[1]== ob['Food'].worldPosition[1]:
                ob['Food'].worldPosition[0]=int(random()*16)-8
                ob['Food'].worldPosition[1]=int(random()*16)-8
                own['Tails'].append(sce.addObject('Tail'))
                own['Tails'][-1].worldPosition=own['Tails'][-2].worldPosition
                own['Score']+=1
         
    for i in own['Tails']:
        if i.worldPosition==own.worldPosition:
            bge.logic.endGame()   
    for i in own['Tails']:
        if i.worldPosition==ob['Food'].worldPosition:
            ob['Food'].worldPosition[0]=int(random()*16)-8
            ob['Food'].worldPosition[1]=int(random()*16)-8
    if own.worldPosition[0]< -8:bge.logic.endGame()   
    if own.worldPosition[0]>  8:bge.logic.endGame()  
    if own.worldPosition[1]>  8:bge.logic.endGame()  
    if own.worldPosition[1]< -8:bge.logic.endGame()  

main()
