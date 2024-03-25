import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import './media_screens.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from 'react-router-dom';
import MouseMove from './components/MouseMove';

// Material Dashboard 2 React Context Provider
import { MaterialUIControllerProvider } from './context';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<BrowserRouter>
		<React.StrictMode>
			<MaterialUIControllerProvider>
				<App />
				<MouseMove></MouseMove>
			</MaterialUIControllerProvider>
		</React.StrictMode>
	</BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
