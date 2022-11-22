import React from 'react'
import './cuentas.css';

export const Cuentas = (props) => {
    console.log(props)
  return (
            <div className="container-t-graph">
                <div className='fix-title'>
                    <p>{props.titulo}</p>
                </div>
                <div className='container'>
                    <div className='divide-container-top'>
                        <div className='debito'>
                            <div className='data'>
      {props.debito.map((item, key) => {
          return(
              <p key={key}> 
              {item}
              </p>
          )
      })}
                            </div>
                        </div>
                    </div>
                    <div className='divide-container'></div>
                    <div className='divide-container-top'>
                        <div className='credito'>
                            <div className='data'>
      {props.credito.map((item, key) => {
          return(
              <p key={key}> 
              {item}
              </p>
          )
      })}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
  )
}

export default Cuentas;
