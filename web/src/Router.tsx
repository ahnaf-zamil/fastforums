import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { RegisterPage } from "./pages/auth/Register";

export const Router: React.FC = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<h1>Homepage</h1>} />

				{/* Auth routes */}
				<Route path="/login" element={<h1>Login page</h1>} />
				<Route path="/register" element={<RegisterPage />} />
			</Routes>
		</BrowserRouter>
	);
};
