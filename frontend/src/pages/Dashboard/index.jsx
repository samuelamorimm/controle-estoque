import React from "react";
import SideBar from "../../components/SideBar";
import Header from "../../components/Header";


export default function Dashboard(){
    return(
        <div className="container font-poppins min-w-full h-max text-white ">
            <Header/>
            <SideBar/>
        </div>
    )
}