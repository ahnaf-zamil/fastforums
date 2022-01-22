import { httpClient } from "./http";
import Routes from "./routes";

export const createUser = async (
	username: string,
	email: string,
	password: string
) => {
	const payload = { username, email, password };
	return await httpClient.post(
		Routes.API_URL + Routes.ENDPOINTS.USERS.CREATE_USER,
		payload
	);
};
