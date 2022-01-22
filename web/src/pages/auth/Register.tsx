import React, { SyntheticEvent, useRef, useState } from "react";
import { PageWrapper } from "../Wrapper";
import PolygonBG from "../../img/auth_polygon.svg";
import { createUser } from "../../api/users";
import axios from "axios";
import LoadingBar, { LoadingBarRef } from "react-top-loading-bar";

export const RegisterPage: React.FC = () => {
	const [error, setError] = useState<null | string>(null);
	const loadingBarRef = useRef<LoadingBarRef>(null);

	const handleSubmit = async (e: SyntheticEvent) => {
		e.preventDefault();
		const targetForm = e.target as typeof e.target & {
			username: { value: string };
			email: { value: string };
			password: { value: string };
		};

		const username = targetForm.username.value;
		const email = targetForm.email.value;
		const password = targetForm.password.value;

		loadingBarRef.current?.staticStart(20);
		try {
			await createUser(username, email, password);
			window.location.href = "/";
		} catch (err) {
			if (axios.isAxiosError(err)) {
				setError(err.response?.data.description);
			}
		} finally {
			loadingBarRef.current?.complete();
		}
	};

	return (
		<PageWrapper title="Register">
			<LoadingBar color="#f11946" ref={loadingBarRef} />
			<div className="h-screen w-full lg:flex">
				<div
					style={{ backgroundImage: `url(${PolygonBG})` }}
					className="w-5/12 h-full hidden lg:flex items-center justify-center flex-col gap-10"
				>
					<h1 className="text-5xl font-bold">Welcome!</h1>
					<p className="w-9/12 text-center text-xl">
						Let's get you started by creating an account. <br />
						<br />
						If you already have an account, click the button below
					</p>
					<div>
						<span className="animate-ping absolute inline-flex h-3 w-3 rounded-full bg-sky-400 opacity-100"></span>
						<button
							onClick={() => (window.location.href = "/login")}
							className="border-2 py-4 w-48 rounded-3xl text-xl shadow-xl transition-all duration-500 hover:bg-[#2966a6]"
						>
							Sign In
						</button>
					</div>
				</div>
				<div className="w-full h-full lg:w-7/12 flex justify-center items-center flex-col">
					{error ? (
						<div className="bg-red-400 p-4 w-8/12 md:w-6/12 lg:w-5/12 text-center mb-10 text-lg">
							{error}
						</div>
					) : null}
					<h1 className="text-center text-4xl font-bold mb-12">
						Create an Account
					</h1>
					<form
						onSubmit={handleSubmit}
						className="w-full flex flex-col gap-4 items-center"
					>
						<input
							className="block w-8/12 md:w-6/12 lg:w-5/12 bg-slate-800 rounded-lg h-12 px-4 focus:ring-0"
							type="text"
							placeholder="Username"
							required={true}
							minLength={3}
							maxLength={30}
							name="username"
						/>
						<input
							className="block w-8/12 md:w-6/12 lg:w-5/12 bg-slate-800 rounded-lg h-12 px-4 focus:ring-0"
							type="email"
							placeholder="Email"
							required={true}
							name="email"
						/>
						<input
							className="block w-8/12 md:w-6/12 lg:w-5/12 bg-slate-800 rounded-lg h-12 px-4 focus:ring-0"
							type="password"
							placeholder="Password"
							required={true}
							minLength={8}
							name="password"
						/>
						<button className="mt-4 py-4 w-40 rounded-3xl text-lg shadow-xl bg-[#2966a6] hover:bg-[#306cab]">
							Sign Up
						</button>
					</form>
					<div className="absolute bottom-2 text-slate-400">
						Copyright &copy; DevGuyAhnaf {new Date().getFullYear()}
					</div>
				</div>
			</div>
		</PageWrapper>
	);
};
