import React, { useState, useContext } from 'react';
import { NavLink } from 'react-router-dom';
import { SafarisContext } from '../App';
import { useAppContext } from '../services/utils';

export default function Header() {
	let [searchTerm, setSearchTerm] = useState('');
	const { auth, handleLogout } = useAppContext();
	let [vacations, setVacations] = useState(true);

	function onSearchChange(e) {
		setSearchTerm(e.target.value)
	}
	function handleSearchSubmit(e) {
		e.preventDefault();
	}

	function handleVacationsClick() {
		setVacations(true)
	}

	function handleStaysClick() {
		setVacations(false)
	};

	return (
		<header className='header px-5 pt-2 pb-5 text-white'>
			<div className='header-nav-container-1 container-fluid d-flex justify-content-between'>
				<h4 className='text-white'>
					<NavLink to='/' exact className='text-white home_link'>
						<span className='spartans_span'>Spartans</span> <span className='safaris_span'>Safaris</span>
					</NavLink>
				</h4>
				<div className='header-nav_1'>
					<p>
						{auth && <NavLink to='/my_bookings' className='text-white nav_links_2'><div className='bookings d-inline'>Manage Bookings <p className='booking_count'>Bookings</p></div></NavLink>}
					</p>
					<p>
						{auth ?
							<button type='button' className='text-white nav_links_2 border-0 bg-transparent ' onClick={handleLogout}>Logout</button>
							:
							<NavLink to='/signin' className='text-white nav_links_2' exact>Login</NavLink>
						}
					</p>
					<p>
						{auth &&
							<NavLink to='/dashboard/dashboard' className='text-white' exact>
								<img src='https://cdn-icons-png.flaticon.com/128/10307/10307911.png' alt='NA' className='profile_img'></img>
							</NavLink>
						}
					</p>
				</div>
			</div>

			<div className='header-nav-container-2 d-flex justify-content-around flex-wrap'>
				<div className='service_div'>
					<NavLink to='/vacations' onClick={handleVacationsClick} className='nav_links_2'>Vacations</NavLink>
				</div>

				<div className='service_div'>
					<NavLink to='/accommodations' onClick={handleStaysClick} className='nav_links_2'>Accommodations & Hotels</NavLink>
				</div>

				<div className='service_div'>
					<a href='https://www.kenya-airways.com/en-us/' className='nav_links_2' target='_blank' rel="noreferrer">
						Flights
					</a>
				</div>

				<div className='service_div'>
					<a href='https://www.pigiame.co.ke/car-hire' className='nav_links_2' target='_blank' rel="noreferrer">
						Car Rentals
					</a>
				</div>

				<div className='service_div'>
					<a href='https://www.uber.com' className='nav_links_2' target='_blank' rel="noreferrer">
						Taxis/Uber
					</a>
				</div>
			</div>

			{vacations ?
				<div className='nav_links_info container mt-3 mb-0'>
					<div>
						<h2> Attractions, activities, and experiences </h2>
						<p> Discover new attractions and experiences to match your interests and travel style </p>
					</div>
				</div>
				:
				<div className='nav_links_info container mt-3 mb-0'>
					<div>
						<h2> Find your next stay </h2>
						<p> Search deals on hotels, homes, and much more... </p>
					</div>
				</div>
			}

			<div className='search_form py-1 px-2'>
				<form className='d-flex gap-1' onSubmit={handleSearchSubmit}>
					<input type='text' className='destination_input' name='destination' placeholder='Destination' onChange={onSearchChange} autoComplete='off'></input>
					<input type='submit' value="Search" className='search_btn text-white bg-primary'></input>
				</form>
			</div>
		</header>
	)
};