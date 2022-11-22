import React from 'react';
import './fondo.css';
import { FaCoins, FaCashRegister, FaMoneyBillAlt, FaPiggyBank } from "react-icons/fa";

export const Fondo = (props) => {
    return (
        <div>

            <table>
                <tr>
                    <td>
                        <FaCoins size={30} />  Ingresos
                        <div>
                            {props.activo}
                        </div>
                    </td>
                    <td><FaCashRegister size={30} /> Deudas 
                        <div>
                            {props.pasivo}
                        </div>
                    </td>
                    <td><FaMoneyBillAlt size={30} />  Creditos
                        <div>
                            {props.capital}
                        </div>
                    </td>
                    <td><FaPiggyBank size={30} />  Patrimonio
                        <div>
                            {props.patrimonio}
                        </div>
                    </td>
                </tr>
            </table>


        </div>
    )
}
