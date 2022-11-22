import './App.css';
import { Fondo } from './components/Fondo';
import Cuentas from './components/cuentas';

import axios from 'axios';
import { useEffect, useState, useState2 } from 'react';
import Chart from "react-apexcharts";


const useLoadData = (label, month, year) => {
    const [debres, Setdebres] = useState([])
    const [credres, Setcredres] = useState([])
    const [resultado, Setresultado] = useState()
    var debito = []
    var credito = []
    useEffect(() => {
        if (label == 1) {
            const url = "http://custom_server.localhost:5000/contabilidad/generate_Tactivo/" + month.toString() + '/' + year.toString()
            axios.get(url)
                .then(res => {
                    res.data.debito.map(({ value }) => {
                        if (value != undefined) {
                            debito.push(value)
                        }
                    })
                    res.data.credito.map(({ value }) => {
                        if (value != undefined) {
                            credito.push(value)
                        }
                    })
                    Setdebres(debito)
                    Setcredres(credito)
                    Setresultado(res.data.resultado)
                })
        }
        if (label == 2) {
            const url = "http://custom_server.localhost:5000/contabilidad/generate_Tpasivo/" + month.toString() + '/' + year.toString()
            axios.get(url)
                .then(res => {
                    debito.push(res.data.debito["banco"])
                    debito.push(res.data.debito["ganancia"])
                    debito.push(res.data.debito["salarios"])
                    credito.push(res.data.credito)
                    Setdebres(debito)
                    Setcredres(credito)
                    Setresultado(res.data.resultado)
                })
        }
        if (label == 3) {
            const url = "http://custom_server.localhost:5000/contabilidad/generate_Tcapital/" + month.toString() + '/' + year.toString()
            axios.get(url)
                .then(res => {
                    res.data.debito.activo.map(({ value }) => {
                        if (value != undefined) {
                            debito.push(value)
                        }
                    })
                    credito.push(res.data.credito.pasivo)
                    res.data.credito.activo.map(({ value }) => {
                        if (value != undefined) {
                            credito.push(value)
                        }
                    })
                    Setdebres(debito)
                    Setcredres(credito)
                    Setresultado(res.data.resultado)
                })
        }
        if (label == 4) {
            const url = "http://custom_server.localhost:5000/contabilidad/generate_Tpatrimonio/" + month.toString() + '/' + year.toString()
            axios.get(url)
                .then(res => {
                    res.data.debito.map(({ value }) => {
                        if (value != undefined) {
                            debito.push(value)
                        }
                    })
                    res.data.credito.map(({ value }) => {
                        if (value != undefined) {
                            credito.push(value)
                        }
                    })
                    Setdebres(debito)
                    Setcredres(credito)
                    Setresultado(res.data.resultado)
                })
        }
    }, [])
    return [debres, credres, resultado]
}


function App() {
    const [state, setState] = useState({
        options: {
            chart: {
                id: "basic-bar"
            },
            xaxis: {
                categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
            }
        },
        series: [
            {
                name: "series-1",
                data: [30, 40, 45, 50, 49, 60, 70, 91]
            }
        ]
    })
    const [state2, setState2] = useState({
        options: {
            chart: {
                id: "basic-bar"
            },
            xaxis: {
                categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
            }
        },
        series: [
            {
                name: "series-1",
                data: [30, 40, 45, 50, 49, 60, 70, 91]
            },
            {
                name: "series-2",
                data: [3, 44, 14, 25, 30, 70, 23, 66]
            }
        ]
    })


    const activo = useLoadData(1, 2022, 10)
    const pasivo = useLoadData(2, 2022, 10)
    const capital = useLoadData(3, 2022, 10)
    const patrimonio = useLoadData(4, 2022, 10)
    const activo_debito = activo[0], activo_credito = activo[1], activo_resultado = activo[2]
    const pasivo_debito = pasivo[0], pasivo_credito = pasivo[1], pasivo_resultado = pasivo[2]
    const capital_debito = capital[0], capital_credito = capital[1], capital_resultado = capital[2]
    const patrimonio_debito = patrimonio[0], patrimonio_credito = patrimonio[1], patrimonio_resultado = patrimonio[2]
    return (
        <div className="App">
            <header className="App-header" >
                <h1>CIERRE CONTABLE</h1>

            </header>

            <Fondo activo={activo_resultado} pasivo={pasivo_resultado} capital={capital_resultado} patrimonio={patrimonio_resultado} />

            <header className="App-header" >
                <h1>CUENTAS T</h1>

            </header>
            <div className='container-all'>
                <Cuentas titulo={"ACTIVOS"} debito={activo_debito} credito={activo_credito} />
                <Cuentas titulo={"PASIVOS"} debito={pasivo_debito} credito={pasivo_credito} />
                <Cuentas titulo={"PATRIMONIO"} debito={patrimonio_debito} credito={patrimonio_credito} />
                <Cuentas titulo={"CAPITAL"} debito={capital_debito} credito={capital_credito} />
            </div>

            <header className="App-header" >
                <h1>GRAFICOS</h1>

            </header>
            <table align='center'>
                <tr>
                    <td> <Chart
                        options={state.options}
                        series={state.series}
                        type="line"
                        width="400"
                    />
                    </td>
                    <td>
                        <Chart
                            options={state2.options}
                            series={state2.series}
                            type="line"
                            width="400"
                        />
                    </td>
                </tr>
            </table>

            <header className="App-header" >
                <table>
                    <button className='boton' onClick={""}> Prev month</button>
                    <button className='boton' onClick={""}> Next month</button>
                </table>
            </header>
        </div>
    );
}

export default App;
