import React from "react";
import { TbPresentationAnalyticsFilled } from "react-icons/tb";
import { FaArrowDown, FaArrowUp, FaBox, FaTools } from "react-icons/fa";
import { MdCategory } from "react-icons/md";
import { FaTruck } from "react-icons/fa";
import { HiAdjustments } from "react-icons/hi";

export default function SideBar() {

    // função para retornar um item da sidebar de forma mais prática
    function itemAside(icon, title){
        return(
            <li className="flex gap-2 items-center  p-3 rounded-xl cursor-pointer hover:bg-gray-700">
                <span>{icon}</span> <span>{title}</span>
            </li>
        )
    }

    return(
        <aside className="container rounded-xl shadow bg-gray-800 p-4 m-4 w-1/5 h-screen text-sm text-gray-300 flex flex-col gap-4 overflow-y-scroll">
            <section className="flex flex-col gap-3">
                <h4>PRINCIPAL</h4>
                <ul className=" flex flex-col gap-3">
                    {itemAside(<TbPresentationAnalyticsFilled/>, 'Dashboard')}
                    {itemAside(<FaBox/>, 'Produtos')}
                    {itemAside(<MdCategory/>, 'Categorias')}
                    {itemAside(<FaTruck/>, 'Fornecedores')}
                </ul>
            </section>

            <section className="flex flex-col gap-3">
                <h4>MOVIMENTAÇÕES</h4>
                <ul className="flex flex-col gap-3">
                    {itemAside(<FaArrowDown/>, 'Entradas')}
                    {itemAside(<FaArrowUp/>, 'Saídas')}
                    {itemAside(<HiAdjustments/>, 'Ajustes')}
                </ul>
            </section>
        </aside>
    )
}