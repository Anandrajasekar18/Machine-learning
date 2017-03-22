function plotDB(theta,X,y)
  plotData(X(:,2:3), y);
  hold on
  if size(X,2)<=2
  x = X(:,2);

    
    y = (-1./theta(3)).*(theta(2).*x + theta(1));

   
    plot(x, y)
    
   
    legend('Admitted', 'Not admitted', 'Decision Boundary')
   
   else 
      u=linspace(max(X(:,2)),min(X(:,2)),100);
      v=linspace(max(X(:,3)),min(X(:,3)),100);
      z= zeros(length(u),length(v));
      for i = 1: length(u)
      	for j = 1: length(u)
      		z(i,j)=mapFeature(u(i),v(j))*theta ;
      	end 
     end
     end
     z=z';
    contour(u,v,z,[0,0]);  	

  %x=[max(X(2)),min(X(2))];
  %Y= (-1/theta(3))*(theta(2)*x+ theta(1));
  %plot(x,Y,'-')
end