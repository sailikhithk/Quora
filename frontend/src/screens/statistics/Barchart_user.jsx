import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import { loadUserStats } from '../../redux/action';





const BarchartUser = () => {

    const dispatch=useDispatch();
    const [userGraphs1,setUserGraphs1]=useState([])
    const [userGraphs2,setUserGraphs2]=useState([])

    const [userCard1,setUserCard1]=useState([])
    const [userCard2,setUserCard2]=useState([])

    const { userStats } = useSelector((state) => state.data);


    useEffect(()=>{
        dispatch(loadUserStats());
    },[]) 

    useEffect(()=>{
if(userStats && userStats?.graphs){
    setUserGraphs1(userStats?.graphs.length>0?userStats?.graphs[0].data:[])
    setUserGraphs2(userStats?.graphs.length>0?userStats?.graphs[1].data:[])
}

if(userStats && userStats?.cards){
    setUserCard1(userStats?.cards.length>0?userStats?.cards[0].data:[])
    setUserCard2(userStats?.cards.length>0?userStats?.cards[1].data:[])
}


    },[userStats])


  return (
    <div style={{display:"grid", gridTemplateRows:"1fr 1fr",gridTemplateColumns:"1fr 1fr",gap:"20px"}} className="h-full w-full overflow-y-scroll">
<div>
    <BarChart width={500} height={300} data={userGraphs1} 
    margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      {/* <CartesianGrid strokeDasharray="3 3" /> */}
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="value" fill="#bb86fc" />
    </BarChart>
    <h1 style={{fontWeight: 'bold',fontSize:"20px",textAlign:"center"}}>Percentage of marks scored Vs Quiz</h1>

    </div>

<div>
    <BarChart width={500} height={300} data={userGraphs2}>
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="value" fill="#bb86fc" />
    </BarChart>
    <h1 style={{fontWeight: 'bold',fontSize:"20px",textAlign:"center"}}>No.of attemps to qualify Vs Quiz</h1>

    </div>
    </div>
  );
};

export default BarchartUser;