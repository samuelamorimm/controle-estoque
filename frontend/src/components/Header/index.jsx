import React from "react";

export default function Header() {
    return (
        <header className="container flex items-center bg-gray-800 min-w-full bg-fixed h-20 ">
            <div className="border border-gray-600 h-full flex items-center px-8">
                <h1 className="font-poppins text-4xl font-bold">Controle<span className="text-blue-400">Max</span></h1>
            </div>

            <div className="border border-gray-600 h-full flex items-center px-4 w-full">
                <button></button>
            </div>
        </header>
    )
}