import React, { ReactNode } from "react";
import { Helmet } from "react-helmet";

interface Props {
	title: string;
	children: ReactNode;
}

export const PageWrapper: React.FC<Props> = ({ title, children }) => {
	return (
		<div className="w-full bg-[#0c1221] text-white">
			<Helmet>
				<title>{title} - FastForums</title>
			</Helmet>
			{children}
		</div>
	);
};
